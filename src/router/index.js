import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
  history: createWebHashHistory(), // hash 模式
  routes: [
    {
      name: "index",
      path: "/",
      component: () => import("@/views/Index.vue"),
    },
    {
      name: "classification",
      path: "/classification",
      component: () => import("@/views/TextClassification.vue"),
    },
    {
      name: "dashboard",
      path: "/dashboard",
      component: () => import("@/views/Dashboard.vue"),
    },
    {
      name: "signin",
      path: "/signin",
      component: () => import("@/views/SignIn.vue"),
    },
  ],
});

export default router;
