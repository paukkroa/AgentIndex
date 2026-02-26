import httpx
import asyncio

async def test():
    url = "https://www.purina.com/dogs/dog-breeds/collections"
    headers = {
        "User-Agent": "AgenticIndex/0.1",
    }
    
    async with httpx.AsyncClient(follow_redirects=True, timeout=10.0) as client:
        print("Testing with AgenticIndex/0.1 header...")
        try:
            resp = await client.get(url, headers=headers)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                print(f"Success! Content length: {len(resp.text)}")
            else:
                print(f"Failed with {resp.status_code}")
                print(f"Headers: {resp.headers}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
