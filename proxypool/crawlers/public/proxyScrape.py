from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
from loguru import logger
# import SimpleHTTPServer;
# import SocketServer;  


BASE_URL = 'http://127.0.0.1:7777/proxyscrape_1000_http_proxies.txt'
# PORT = 7777; #server port
# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler;
# httpd = SocketServer.TCPServer(("127.0.0.1", PORT), Handler); 

class ProxyScrapeCrawler(BaseCrawler):
    """
    ipidea crawler, http://tiqu.linksocket.com:81/abroad?num=20&type=2&lb=1&sb=0&flow=1&regions=kr&n=0
    """
    urls = [BASE_URL]
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36",
    }

    @logger.catch
    def crawl(self):
        """
        crawl main method
        """
        for url in self.urls:
            logger.info(f'fetching {url}')
            with open('/Users/anonymity/Desktop/COI/proxyscrape_1000_http_proxies.txt','r') as f:
                for proxy in self.parse(f):
                    logger.info(f'fetched proxy {proxy.string()} from {url}')
                    yield proxy
            f.close()        
    
    def parse(self, file):
        """
        parse html file to get proxies
        :return:
        """
        try:
            proxies = file.readlines()
        except ValueError:
            print('cannot load the txt file from http://127.0.0.1:7777/proxyscrape_1000_http_proxies.txt')
            exit(-1)
        for proxy in proxies:
            print(proxy)
            strls = proxy.split(':')
            yield Proxy(host=strls[0].strip(), port=strls[1].strip())


if __name__ == '__main__':
    # httpd.serve_forever();
    crawler = ProxyScrapeCrawler()
    for proxy in crawler.crawl():
        print(proxy)
