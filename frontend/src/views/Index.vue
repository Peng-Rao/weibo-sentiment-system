<script setup>
import NavigationBar from "@/components/Common/NavigationBar.vue";
import SearchBar from "@/components/Common/SearchBar.vue";
import PieChart from "@/components/Charts/PieChart.vue";
import BarChart from "@/components/Charts/BarChart.vue";
import MapChart from "@/components/Charts/MapChart.vue";
</script>

<template>
  <div>
    <!-- Top navigation bar -->
    <navigation-bar></navigation-bar>

    <!-- Main content area with gradient background -->
    <search-bar></search-bar>
    <pie-chart style="height: 100vh"></pie-chart>
    <map-chart style="height: 100vh"></map-chart>
    <bar-chart style="height: 100vh"></bar-chart>
  </div>
</template>

