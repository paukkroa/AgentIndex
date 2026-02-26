"""Token and dollar cost tracking for evaluation runs."""

from __future__ import annotations

from dataclasses import dataclass, field

from evaluation.config import MODEL_PRICING


@dataclass
class QueryCost:
    """Cost breakdown for a single query."""

    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    embedding_tokens: int = 0

    @property
    def input_cost_usd(self) -> float:
        pricing = MODEL_PRICING.get(self.model, {"input": 0.0, "output": 0.0})
        return self.input_tokens * pricing["input"] / 1000

    @property
    def output_cost_usd(self) -> float:
        pricing = MODEL_PRICING.get(self.model, {"input": 0.0, "output": 0.0})
        return self.output_tokens * pricing["output"] / 1000

    @property
    def embedding_cost_usd(self) -> float:
        pricing = MODEL_PRICING.get("text-embedding-3-small", {"input": 0.0, "output": 0.0})
        return self.embedding_tokens * pricing["input"] / 1000

    @property
    def total_cost_usd(self) -> float:
        return self.input_cost_usd + self.output_cost_usd + self.embedding_cost_usd

    def to_dict(self) -> dict[str, float]:
        return {
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "embedding_tokens": self.embedding_tokens,
            "input_cost_usd": self.input_cost_usd,
            "output_cost_usd": self.output_cost_usd,
            "embedding_cost_usd": self.embedding_cost_usd,
            "total_cost_usd": self.total_cost_usd,
        }


@dataclass
class ExperimentCostTracker:
    """Aggregate cost tracker across an entire experiment."""

    system_name: str
    query_costs: list[QueryCost] = field(default_factory=list)

    def add_query(self, model: str, input_tokens: int, output_tokens: int, embedding_tokens: int = 0) -> QueryCost:
        cost = QueryCost(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            embedding_tokens=embedding_tokens,
        )
        self.query_costs.append(cost)
        return cost

    @property
    def total_input_tokens(self) -> int:
        return sum(q.input_tokens for q in self.query_costs)

    @property
    def total_output_tokens(self) -> int:
        return sum(q.output_tokens for q in self.query_costs)

    @property
    def total_embedding_tokens(self) -> int:
        return sum(q.embedding_tokens for q in self.query_costs)

    @property
    def total_cost_usd(self) -> float:
        return sum(q.total_cost_usd for q in self.query_costs)

    @property
    def mean_cost_per_query(self) -> float:
        if not self.query_costs:
            return 0.0
        return self.total_cost_usd / len(self.query_costs)

    def summary(self) -> dict[str, float | int | str]:
        return {
            "system": self.system_name,
            "num_queries": len(self.query_costs),
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_embedding_tokens": self.total_embedding_tokens,
            "total_cost_usd": self.total_cost_usd,
            "mean_cost_per_query_usd": self.mean_cost_per_query,
        }
