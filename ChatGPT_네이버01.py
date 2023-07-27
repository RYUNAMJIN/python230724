import requests
from bs4 import BeautifulSoup

def crawl_blog_info(search_keyword):
    # Construct the search URL with the search_keyword
    search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

    # Send a request to get the HTML content of the search results page
    response = requests.get(search_url)
    response.raise_for_status()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the blog posts' containers
    blog_containers = soup.select('li.sh_blog_top')

    # Initialize a list to store the blog information
    blog_info_list = []

    # Extract information from each blog post container
    for container in blog_containers:
        blog_address = container.select_one('a.sh_blog_title')['href']
        post_title = container.select_one('a.sh_blog_title').text
        post_date = container.select_one('.txt_inline').text.strip()

        blog_info = {
            'blog_address': blog_address,
            'post_title': post_title,
            'post_date': post_date
        }
        blog_info_list.append(blog_info)

    return blog_info_list

if __name__ == "__main__":
    search_keyword = input("Enter the word to search: ")
    blog_info_list = crawl_blog_info(search_keyword)

    # Display the results
    for idx, blog_info in enumerate(blog_info_list, 1):
        print(f"Blog {idx} - Title: {blog_info['post_title']}")
        print(f"Blog {idx} - Address: {blog_info['blog_address']}")
        print(f"Blog {idx} - Date: {blog_info['post_date']}")
        print()
