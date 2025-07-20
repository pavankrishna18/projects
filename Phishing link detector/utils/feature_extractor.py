# ==== File: utils/feature_extractor.py ====
import re

def extract_features(url):
    return {
        'url_length': len(url),
        'has_ip': 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        'has_https': 1 if 'https' in url.lower() else 0,
        'has_at': 1 if '@' in url else 0,
        'count_dots': url.count('.'),
        'count_hyphen': url.count('-'),
        'count_slash': url.count('/'),
        'has_suspicious_word': 1 if re.search(r'login|secure|account|update|banking', url.lower()) else 0
    }


