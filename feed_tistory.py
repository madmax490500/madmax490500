import feedparser
import time

def parse_feed(url):
    rss_feed = feedparser.parse(url)
    if rss_feed.bozo:
        raise Exception(f"Error parsing feed: {rss_feed.bozo_exception}")
    return rss_feed

def generate_markdown(entries, max_post):
    markdown_text = """
### 시스템엔지니어가 사용하는 코드 저장소입니다.
### This repository is used by SRE.

### 지속적인 목표 (SRE 목표)
* 서비스의 안정성을 유지하면서 변화를 최대한 수용한다.
* 시스템의 상태와 가용성을 꾸준히 모니터링 한다.
* 어떤 기능에 대해 문제가 발생하면 이에 대해 긴급 대응을 한다.
* 시스템의 변화를 추적하고 관리한다.
* 수요를 예측하고, 계획을 세운다.
* 이를 통해 서비스의 수용력을 확보하고, 효율성을 향상한다.


## ✅ Latest Blog Posts

"""  # list of blog posts will be appended here

    for idx, feed in enumerate(entries):
        if idx >= max_post:
            break
        feed_date = feed.get('published_parsed')
        if feed_date:
            formatted_date = time.strftime('%Y/%m/%d', feed_date)
        else:
            formatted_date = "Unknown date"
        
        title = feed.get('title', 'No title')
        link = feed.get('link', '#')
        
        markdown_text += f"[{formatted_date} - {title}]({link}) <br/>\n"
    
    return markdown_text

def write_to_file(content, file_path):
    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(content)
        print(f"{file_path} file has been written.")

def main():
    url = "https://vitta.tistory.com/rss"
    max_post = 5

    rss_feed = parse_feed(url)
    entries = rss_feed.get('entries', [])
    print(f"Number of entries: {len(entries)}")

    markdown_text = generate_markdown(entries, max_post)
    print("Generated markdown text:")
    print(markdown_text)

    write_to_file(markdown_text, "README.md")

if __name__ == "__main__":
    main()
