<?php
$CSP = "default-src 'none'; manifest-src 'self'; connect-src *; script-src 'self' 'unsafe-eval'; style-src 'self'; font-src 'self'; img-src 'self' data: blob:; media-src blob:; object-src blob:; sandbox allow-same-origin allow-scripts allow-forms allow-popups allow-modals";
header('Content-Security-Policy: ' . $CSP );
