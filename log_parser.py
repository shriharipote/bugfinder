import re

class LogParser:
    def parse_log(self, log_content):
        errors = []
        lines = log_content.strip().split('\n')
        
        # Better multi-line error pattern
        error_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?(ERROR|CRITICAL|Exception|Exception:).*', re.IGNORECASE)
        
        current_error = None
        stack_trace = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            match = error_pattern.search(line)
            if match:
                # Save previous error if exists
                if current_error:
                    errors.append({
                        "timestamp": current_error["timestamp"],
                        "level": current_error["level"],
                        "message": current_error["message"],
                        "stack_trace": "\n".join(stack_trace)
                    })
                
                current_error = {
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "message": line.split(match.group(2), 1)[1].strip() if match.group(2) in line else line
                }
                stack_trace = []
            elif current_error:
                stack_trace.append(line)
        
        # Don't forget the last error
        if current_error:
            errors.append({
                "timestamp": current_error["timestamp"],
                "level": current_error["level"],
                "message": current_error["message"],
                "stack_trace": "\n".join(stack_trace)
            })
        
        return errors