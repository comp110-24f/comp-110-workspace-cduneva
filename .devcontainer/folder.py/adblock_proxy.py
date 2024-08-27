from mitmproxy import http

# List of ad-serving domains to block
ad_domains = [
    "www.youtube.com"
]

def request(flow: http.HTTPFlow) -> None:
    # Check if the request is to an ad-serving domain
    if any(domain in flow.request.pretty_host for domain in ad_domains):
        flow.response = http.Response.make(
            403,  # HTTP status code for Forbidden
            b"Blocked by adblock proxy",
            {"Content-Type": "text/plain"}
        )

# Run the proxy server
if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    mitmdump(["-s", __file__])
