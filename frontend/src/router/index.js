import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/feed'  // Redirects '/' to '/feed'
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/registration/SignupView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/registration/LoginView.vue')
    },
    {
      path: '/feed',
      name: 'feed',
      component: () => import('../views/feed/FeedView.vue')
    },
    {
      path: '/messages',
      name: 'messages',
      component: () => import('../views/conversation/MessagesView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/feed/SearchView.vue')
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: () => import('@/views/profile/ProfileView.vue'),
      props: true
    }
  ]
})

export default router
