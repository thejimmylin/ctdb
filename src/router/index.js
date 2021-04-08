import { createRouter, createWebHistory } from 'vue-router'
import News from '../views/News.vue'

const routes = [
  {
    path: '',
    redirect: '/news',
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
