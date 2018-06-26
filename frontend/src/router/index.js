import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import FAQ from '@/components/FAQ';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/faq',
      name: 'faq',
      component: FAQ,
    },
  ],
  mode: 'history',
});
