import argparse
import json
import logging
import re
import time
import urllib.request

from prometheus_client import Gauge, start_http_server


class Technitium_exporter:
    def __init__(self, url, username, password, token):
        self.api_url = f"{url}/api"
        self.login_url = f"{self.api_url}/login?user={username}&pass={password}"
        self.status_url = f"{self.api_url}/getStats?type=lastDay"
        self.stat_prefix = "technitium"
        self.stats = None
        self.token = token
        self.generate_export()

    def get_auth_token(self):
        try:
            with urllib.request.urlopen(self.login_url) as req:
                data = req.read()
                json_text = json.loads(data)
                if "token" in json_text.keys():
                    token = json_text["token"]
                else:
                    logging.warning("Unable to get token")
            self.token = token
        except Exception as e:
            logging.error(e)
            logging.error("Check that your url, user, and password are correct")
            exit(1)

    def get_stats(self):
        if self.token is None:
            self.get_auth_token()
        try:
            with urllib.request.urlopen(f"{self.status_url}&token={self.token}") as req:
                data = req.read()
                json_text = json.loads(data)
                if json_text["status"] == "ok":
                    self.stats = json_text["response"]
        except Exception as e:
            logging.error(e)
            logging.error("Unable to get Auth Token from the server")

    def generate_looped_guage_stat(self, stat_name, description, labels):
        stat = Gauge(f"{self.stat_prefix}_{camel_to_snake(stat_name)}", description, labels)
        for item in self.stats[stat_name]:
            stat.labels(item["name"]).set(item["hits"])

    def get_looped_stats(self):
        stats = [
            {
                "name": "topBlockedDomains",
                "description": "Top blocked domains",
                "labels": ["domain"],
            },
            {
                "name": "topDomains",
                "description": "Top allowed domains",
                "labels": ["domain"],
            },
            {"name": "topClients", "description": "Top clients total requests", "labels": ["host"]},
        ]
        for stat in stats:
            self.generate_looped_guage_stat(stat["name"], stat["description"], stat["labels"])

    def generate_single_guage_stat(self, stat_name, description):
        stat = Gauge(f"{self.stat_prefix}_{camel_to_snake(stat_name)}", description)
        stat.set(self.stats["stats"][stat_name])

    def get_single_stats(self):
        stats = [
            {
                "name": "blockListZones",
                "description": "Number of domain names listed in blocked zones",
            },
            {
                "name": "allowedZones",
                "description": "Allowed zones allows to add exception to unblock domain names listed in blocked zones",
            },
            {
                "name": "blockedZones",
                "description": "Number of blocked zones",
            },
            {
                "name": "cachedEntries",
                "description": "The total number of queries that were resolved using data available in the server's cache.",
            },
            {
                "name": "totalAuthoritative",
                "description": "The total number of queries that were resolved from the zones hosted locally on the DNS server.",
            },
            {
                "name": "totalBlocked",
                "description": 'The total number of queries this DNS server blocked by responding with "0.0.0.0" (or "::" for AAAA) for A record request.',
            },
            {
                "name": "totalCached",
                "description": "The total number of queries that were resolved using data available in the server's cache.",
            },
            {
                "name": "totalClients",
                "description": "The total number of unique clients based on IP address of the queries.",
            },
            {
                "name": "totalNoError",
                "description": "The total number of queries that were responded positively by the server. ",
            },
            {
                "name": "totalNxDomain",
                "description": "The server will try to resolve a domain name in the query and if the domain name does not exists, it will receive a NX Domain response code which is also relayed as a response to the original query.",
            },
            {
                "name": "totalQueries",
                "description": "These are the total number of queries the DNS server has received from all clients.",
            },
            {
                "name": "totalRecursive",
                "description": "The total number of queries that were resolved partially or fully resolved by recursive resolution.",
            },
            {
                "name": "totalRefused",
                "description": "The total number of queries this DNS server refused to resolve.",
            },
            {
                "name": "totalServerFailure",
                "description": "The total number of queries that the server failed to respond positively.",
            },
            {
                "name": "zones",
                "description": "The total number of zones on the Technitium server",
            },
        ]

        for stat in stats:
            self.generate_single_guage_stat(stat["name"], stat["description"])

    def generate_export(self):
        self.get_stats()
        self.get_looped_stats()
        self.get_single_stats()


def camel_to_snake(name):
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def main():
    parser = argparse.ArgumentParser("Technitium Prometheus Exporter")
    parser.add_argument("-a", "--address", help="Technitium server address. e.g http://10.0.0.253")
    parser.add_argument("-p", "--port", help="Technitium webui port", default=5380)
    parser.add_argument("-U", "--user", help="UI Username")
    parser.add_argument("-P", "--password", help="UI Password")
    parser.add_argument("-t", "--token", help="API Token")
    parser.add_argument("-w", "--webserver-port", help="Port used by the webserver", default=8080)
    args = parser.parse_args()

    exporter = Technitium_exporter(f"{args.address}:{args.port}", args.user, args.password, args.token)
    start_http_server(args.webserver_port)
    logging.info(f"Run on port {args.webserver_port}")
    while True:
        exporter.get_stats()
        time.sleep(1800)


if __name__ == "__main__":
    main()
