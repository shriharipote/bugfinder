class BugAnalyzer:
    def analyze(self, errors):
        analysis = []
        for error in errors:
            root_cause = self._detect_root_cause(error["message"], error["stack_trace"])
            analysis.append({
                "error": error,
                "root_cause": root_cause["cause"],
                "likely_file": root_cause["file"],
                "line_number": root_cause["line"],
                "severity": root_cause["severity"],
                "suggestion": root_cause["fix"]
            })
        return analysis

    def _detect_root_cause(self, message, stack):
        keywords = {
            "NoneType": {"cause": "Null Reference", "fix": "Add null check before accessing object"},
            "IndexError": {"cause": "Array index out of range", "fix": "Check array length before access"},
            "KeyError": {"cause": "Missing dictionary key", "fix": "Use .get() or check key existence"},
            "Connection": {"cause": "Database/Network issue", "fix": "Check connection string / firewall"},
            "FileNotFound": {"cause": "Missing file", "fix": "Verify file path and existence"}
        }
        
        for key, data in keywords.items():
            if key in message or key in stack:
                return {
                    "cause": data["cause"],
                    "file": "Check stack trace",
                    "line": "See traceback",
                    "severity": "High",
                    "fix": data["fix"]
                }
        
        return {
            "cause": "Unknown / Custom error",
            "file": "Unknown",
            "line": "N/A",
            "severity": "Medium",
            "fix": "Review stack trace and debug step by step"
        }