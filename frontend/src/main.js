import { createApp } from 'vue'
import App from './App.vue'

import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
// import '@/assets/style.css?v=3.0.4'
// import '@/assets/dashboard.css'
import '@/plugins/webfontloader'
import '@/plugins/fontawesome'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'

const pinia = createPinia({
  
})

const app = createApp(App)
app.use(router)
app.use(pinia)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
