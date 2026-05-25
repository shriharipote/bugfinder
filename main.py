from log_parser import LogParser
from bug_analyzer import BugAnalyzer

def main():
    print("🚀 BugFinder - Error Log Analyzer")
    print("=" * 60)
    
    # Sample log for testing
    sample_log = """
2026-05-25 10:15:23 ERROR NullPointerException: Cannot invoke 'str.strip()' on NoneType object
    at com.example.UserService.getUser(UserService.java:45)
    at com.example.Main.main(Main.java:12)
"""
    
    parser = LogParser()
    analyzer = BugAnalyzer()
    
    errors = parser.parse_log(sample_log)
    results = analyzer.analyze(errors)
    
    for result in results:
        print(f"\n🔴 Error: {result['error']['message']}")
        print(f"📍 Root Cause: {result['root_cause']}")
        print(f"📂 File/Line: {result['likely_file']} : {result['line_number']}")
        print(f"🛠️  Suggested Fix: {result['suggestion']}")
        
        if result['error'].get('stack_trace'):
            print(f"📋 Stack Trace:\n{result['error']['stack_trace']}")
        
        print("-" * 70)


if __name__ == "__main__":
    main()