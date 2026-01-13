from http.server import HTTPServer, BaseHTTPRequestHandler

# 1. 서버가 할 일(로직)을 정의하는 클래스
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 응답 상태 코드 전송 (200: 성공)
        self.send_response(200)
        
        # 헤더 설정 (HTML 콘텐츠임을 알림)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 실제 내용(Body) 전송
        response_text = "<h1>Hello, World!</h1><p>파이썬 내장 서버입니다.</p>"
        self.wfile.write(response_text.encode('utf-8'))

# 2. 서버 실행 설정 (주소와 포트)
server_address = ('', 8000)  # 빈 문자열은 localhost를 의미, 포트는 8000
httpd = HTTPServer(server_address, SimpleHandler)

print("서버가 시작되었습니다: http://localhost:8000")
httpd.serve_forever()