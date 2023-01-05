import { createApp, markRaw } from 'vue'
import App from './App.vue'

import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@/layouts/bootstrap/css/style.css'
import 'mdb-ui-kit/css/mdb.min.css'
import '@/plugins/webfontloader'
import '@/plugins/fontawesome'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'
import { createVueSession } from './plugins/vue-storages'
import { createAxios } from './plugins/axios'

const app = createApp(App)

const session = createVueSession()
const client = createAxios()

const pinia = createPinia({})
pinia.use(({ store }) => {
  store.$session = markRaw(session)
})

app.use(router)
app.use(pinia)
app.use(session)
app.use(client)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
