# FETCH DEPENDENCIES
New-Item -ItemType Directory -Force -Path .\bin
cd .\bin\
curl https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip -OutFile chromedriver.zip
Expand-Archive -LiteralPath .\chromedriver.zip -DestinationPath .
curl https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-29/stable-headless-chromium-amazonlinux-2017-03.zip -OutFile headless-chromium.zip
Expand-Archive -LiteralPath .\headless-chromium.zip -DestinationPath .
Remove-Item * -Filter *.zip 

cd ..

# BUILD PACKAGE
New-Item -ItemType Directory -Force -Path .\build
cp -r src build/.
cp -r bin build/.
cp -r lib build/.
pip install -r requirements.txt -t build/lib/.
cd build
rm .\bin\*.zip
Compress-Archive -Path .\* -DestinationPath build.zip