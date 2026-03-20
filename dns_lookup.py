import dns.resolver


def get_records(domain, record_type):
    records = []

    try:
        answers = dns.resolver.resolve(domain, record_type)

        for rdata in answers:
            records.append(rdata.to_text())

    except dns.resolver.NoAnswer:
        records.append("No record found")

    except dns.resolver.NXDOMAIN:
        records.append("Domain does not exist")

    except Exception as e:
        records.append("Error: " + str(e))

    return records


def get_a_records(domain):
    return get_records(domain, "A")


def get_mx_records(domain):
    return get_records(domain, "MX")


def get_ns_records(domain):
    return get_records(domain, "NS")


def get_txt_records(domain):
    return get_records(domain, "TXT")