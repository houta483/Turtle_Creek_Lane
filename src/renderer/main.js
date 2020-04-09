import Vue from 'vue'
import App from './App'
import Vuex from "vuex"

Vue.use(Vuex)

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {
    followers: true,
    stickerResponses: false,
    storyEngagement: false,
  }
});

/* eslint-disable no-new */
new Vue({
  store,
  components: { App },
  template: '<App/>'
}).$mount('#app')
