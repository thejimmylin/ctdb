import { createRouter, createWebHistory } from 'vue-router'
import News from '../views/News.vue'
import Diary from '../views/Diary.vue'

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
  {
    path: '/diaries',
    name: 'Diary',
    component: Diary
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
