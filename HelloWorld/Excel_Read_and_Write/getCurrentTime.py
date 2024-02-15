from datetime import datetime

class GetCurrentTime:
        def getcurrenttime(self):
                now = datetime.now()
                formatted_time_expression = f'{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}'
                print(formatted_time_expression)
                return formatted_time_expression


