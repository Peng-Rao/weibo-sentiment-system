<script setup>
import NavigationBar from "@/components/Header/HeaderArea.vue";
import SearchBar from "@/components/SearchBar.vue";
import Footer from "@/components/Footer/Footer.vue";
import {computed} from "vue";
import {useSearchStore} from "@/stores/useSearchStore";
const isLoading = computed(() => useSearchStore().isLoading);
const isChartVisible = computed(() => useSearchStore().isChartVisible);

</script>

<template>
    <navigation-bar></navigation-bar>
    <div class="mt-1 border-gray-200 shadow-sm bg-gray-50 md:bg-white border-y dark:bg-gray-800 dark:border-gray-600 ">
        <div class="flex justify-center items-center w-full- h-screen">
            <search-bar v-if="!isLoading && !isChartVisible"></search-bar>
                <div v-if="isLoading" class="loading-animation">
                  Loading...
                </div>
        </div>
    </div>
    <router-view></router-view>
    <Footer></Footer>
</template>

