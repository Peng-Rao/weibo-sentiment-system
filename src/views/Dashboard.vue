<script setup>
import ChartThree from "@/components/Charts/ChartThree.vue";
import ChartTwo from "@/components/Charts/ChartTwo.vue";
import DefaultLayout from "@/layout/DefaultLayout.vue";
import MapChart from "@/components/Charts/MapChart.vue";
import DataStatsOne from "@/components/Dashboard/DataStats.vue";
import TweetTrend from "@/components/Dashboard/TweetTrend.vue";

import { onMounted } from "vue";
import { useRoute } from "vue-router";

// 使用useRoute获取当前路由信息
const route = useRoute();
import { useSearchStore } from "@/stores/useSearchStore.js";

// 设置 store 的搜索关键词
onMounted(() => {
  useSearchStore().setSearchKeyword(route.query.keyword);
});
</script>

<template>
  <DefaultLayout>
    <div
      class="grid grid-cols-1 gap-4 md:grid-cols-2 md:gap-6 xl:grid-cols-4 2xl:gap-7.5"
    >
      <DataStatsOne />
    </div>

    <div
      class="mt-4 grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5"
    >
      <!-- ====== Chart One Start -->
      <tweet-trend />
      <!-- ====== Chart One End -->
      <!-- ====== Map One End -->

      <!-- ====== Table One Start -->
      <!--      <div class="col-span-12 xl:col-span-8">-->
      <!--        <TableOne />-->
      <!--      </div>-->
      <!-- ====== Table One End -->

      <!-- ====== Chat Card Start -->
      <!--      <ChatCard />-->
      <!-- ====== Chat Card End -->
    </div>
  </DefaultLayout>
</template>
