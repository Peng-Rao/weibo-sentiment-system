<script setup>
import {computed} from "vue";
import {useSearchStore} from "@/stores/useSearchStore.js";
import DarkModeSwitcher from "@/components/Header/DarkModeSwitcher.vue";

const searchKeyword = computed(() => useSearchStore().searchKeyword);
</script>

<template>
    <header
        class="sticky top-0 z-999 flex w-auto bg-white drop-shadow-1 dark:bg-boxdark dark:drop-shadow-none"
    >
        <div class="flex flex-grow items-center justify-center py-4 px-4 shadow-2 md:px-6 2xl:px-11">
            <div class="flex items-center gap-3 2xsm:gap-7">
                <ul class="flex items-center gap-2 2xsm:gap-4">
                    <li>
                        <router-link
                            to="/"
                            class="block py-2 px-3 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                        >主页
                        </router-link
                        >
                    </li>
                    <li>
                        <router-link
                            :to="{ path: '/dashboard', query: { keyword: searchKeyword } }"
                            class="block py-2 px-3 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                        >关键词分析
                        </router-link
                        >
                    </li>
                    <li>
                        <router-link
                            to="/classification"
                            class="block py-2 px-3 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                        >文本情感分类
                        </router-link
                        >
                    </li>
                    <li>
                        <DarkModeSwitcher/>
                    </li>
                </ul>
            </div>
        </div>
    </header>
</template>
