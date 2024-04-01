<script setup>
import NavigationBar from "@/components/Header/HeaderArea.vue";
import SearchBar from "@/components/SearchBar.vue";
import Footer from "@/components/Footer/Footer.vue";
import {computed} from "vue";
import {useSearchStore} from "@/stores/useSearchStore";
import DefaultLayout from "@/layout/DefaultLayout.vue";

const isLoading = computed(() => useSearchStore().isLoading);
const isChartVisible = computed(() => useSearchStore().isChartVisible);

</script>

<template>
    <default-layout>
        <!--容器内居中-->
        <div class="w-16 h-40 bg-transparent"></div>
        <div class="mx-auto max-w-screen-2xl p-4 md:p-6 2xl:p-10 flex justify-center">
            <search-bar v-if="!isLoading && !isChartVisible"></search-bar>
            <div v-if="isLoading" class="loading-animation">
                Loading...
            </div>
        </div>
        <div class="w-16 h-100 bg-transparent"></div>
    </default-layout>
</template>

