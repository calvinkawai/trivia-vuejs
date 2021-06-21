import Vue from 'vue'
import Router from 'vue-router'
import AddTeam from '@/components/AddTeam'
import RoundOne from '@/components/RoundOne'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AddTeam',
      component: AddTeam
    },
    {
      path: '/RoundOne',
      name: 'RoundOne',
      component: RoundOne
    }
  ]
})
