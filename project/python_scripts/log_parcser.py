import argparse
from collections import Counter
import re

parser = argparse.ArgumentParser(description="Log analyzer for Apache/Nginx")
parser.add_argument("-f", "--file", required=True, help="Path to access.log")
parser.add_argument("-o", "--output", default="report.html", help="HTML report file")
parser.add_argument(
    "--top", type=int, default=10, help="Number of top IPs/User-Agents to show"
)
args = parser.parse_args()

log_file = args.file
output_file = args.output
number_of_top = args.top

log_pattern = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s"  # IP
    r".*\["
    r"(?P<time>[^\]]+)\]\s"  # час
    r'"(?P<method>\w+)\s(?P<url>\S+)\s'
    r'(?P<protocol>[^"]+)"\s'  # метод, URL, протокол
    r"(?P<status>\d{3})\s"  # статус код
    r"(?P<size>\d+|-)\s"  # розмір
    r'"(?P<referer>[^"]*)"\s'  # реферер
    r'"(?P<user_agent>[^"]*)"'  # User-Agent
)
ips = Counter()
statuses = Counter()
agents = Counter()
with open(log_file) as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            log = match.groupdict()
            ips[log["ip"]] += 1
            statuses[log["status"]] += 1
            agents[log["user_agent"]] += 1

    for ip, count in ips.most_common(number_of_top):
        print(f"{ip}: {count}")
    for status, count in statuses.items():
        print(f"{status}: {count}")
    for ua, count in agents.most_common(number_of_top):
        print(f"{ua}: {count}")


def generate_html(ips, agents, statuses, output_file):
    with open(output_file, "w") as f:
        f.write("<html><head><title>Log Report</title></head><body>")
        f.write("<h1>Log analysis </h1>")

        f.write("<h2>Top IPs</h2><ul>")
        for ip, count in ips.most_common(number_of_top):
            f.write(f"<li>{ip} — {count}</li>")
        f.write("</ul>")

        f.write("<h2>Top User-Agent</h2><ul>")
        for ua, count in agents.most_common(number_of_top):
            f.write(f"<li>{ua} — {count}</li>")
        f.write("</ul>")

        f.write("<h2>HTTP statuses</h2><ul>")
        for status, count in statuses.items():
            f.write(f"<li>{status} — {count}</li>")
        f.write("</ul>")

        f.write("</body></html>")


generate_html(ips, agents, statuses, output_file)
