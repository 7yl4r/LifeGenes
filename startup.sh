echo 'compiling dust templates...'
./node_modules/.bin/duster templates templates/templates.js

echo 'compiling less css...'
./node_modules/.bin/lessc -x ./less/bootstrap.less > ./css/bootstrap.min.css

echo 'transpiling .coffee into .js...'
./node_modules/.bin/coffee --output js/coffee --compile coffee

echo 'browserify-ing module dependencies...'
./node_modules/.bin/browserify js/main.js -o js/bundle.js

echo 'starting server for testing...'
python -m SimpleHTTPServer