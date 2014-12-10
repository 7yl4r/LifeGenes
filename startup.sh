echo 'compiling dust templates...'
./node_modules/.bin/duster templates templates/templates.js

echo 'compiling less css...'
./node_modules/.bin/lessc -x ./less/bootstrap/bootstrap.less > ./css/bootstrap.min.css
./node_modules/.bin/lessc -x ./less/cellStates.less > ./css/cellStates.min.css
./node_modules/.bin/lessc -x ./less/proteins.less > ./css/proteins.min.css

echo 'transpiling .coffee into .js...'
./node_modules/.bin/coffee --output js/coffee --compile coffee

echo 'browserify-ing module dependencies...'
./node_modules/.bin/browserify js/main.js -o js/bundle.js

echo 'starting server for testing...'
python -m SimpleHTTPServer