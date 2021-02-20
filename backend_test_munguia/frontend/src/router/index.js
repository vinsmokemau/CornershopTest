import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ListOrders',
      component: () => import('@/components/Orders/ListOrders.vue')
    },
    {
      path: '/create-menu',
      name: 'CreateMenu',
      component: () => import('@/components/Menu/CreateMenu.vue')
    },
    {
      path: '/menu/:idUser',
      name: 'CreateOrder',
      component: () => import('@/components/Orders/CreateOrder.vue')
    },
  ],
  mode: 'history'
})
