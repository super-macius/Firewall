import random

def generaterandomip():
    return f"192.168.1.{random.randint(0, 20)}"

def checkfirewallrules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.2": "block",
        "192.168.1.4": "block",
        "192.168.1.8": "block",
        "192.168.1.16": "block"
    }

    for _ in range(12):
     ip_address = generate_random_ip()
     action = check_firewall_rules(ip_address, firewall_rules)
     random_number = random.randint(0, 9999)
     print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()