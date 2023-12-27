
# NVM install
``` sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

# NVM setup
export NVM_DIR="$HOME/.nvm"
# This loads nvm
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
# This loads nvm bash_completion
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

# Node install
``` sh
# install last node LTS version
nvm install --lts

# check installed versions
npm -v
node -v
```

# Vue CLI install
``` sh
npm install -g @vue/cli
```

## create a Vue CLI project
``` sh
vue create hello-vue
```

## run server
``` sh
cd hello-vue
$ npm run serve
```
