import Vue from 'vue'
import Router from 'vue-router'
import Unread from '@/components/Unread'
import TabView from "@/components/TabView"
Vue.use(Router)
Vue.config.productionTip = false

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'TabView',
      component: TabView
    },
    {
      path: '/unread',
      name: 'Unread',
      component: Unread
    }
]
})
