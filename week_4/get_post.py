import requests

url = "https://jsonplaceholder.typicode.com/posts/10"
response = requests.get(url)

if response.status_code == 200:
    post_data = response.json()
    print(f"the post title is {post_data['title']}")
    print(f"the post body is {post_data['body']}")
else:
    print("unable to retrieve the data")
    
