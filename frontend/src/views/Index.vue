<script setup>
import NavigationBar from "@/components/common/NavigationBar.vue";
import SearchBar from "@/components/common/SearchBar.vue";
import PieChart from "@/components/charts/PieChart.vue";
import BarChart from "@/components/charts/BarChart.vue";
import MapChart from "@/components/charts/MapChart.vue";
import Footer from "@/components/common/Footer.vue";
</script>

<template>
    <navigation-bar></navigation-bar>
    <div id="mega-menu-full-dropdown" class="mt-1 border-gray-200 shadow-sm bg-gray-50 md:bg-white border-y dark:bg-gray-800 dark:border-gray-600">
        <div class="container mx-auto px-4 py-4">
            <search-bar></search-bar>
            <map-chart style="height: 100vh"></map-chart>
            <pie-chart style="height: 100vh"></pie-chart>
<!--            <bar-chart style="height: 100vh"></bar-chart>-->
        </div>
    </div>
    <router-view></router-view>
    <Footer></Footer>
</template>

