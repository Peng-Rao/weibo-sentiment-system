import axiosInstance from '@/api/axiosInstance';

export const startCrawler = async (url, keyword) => {
    try {
        const response = await axiosInstance.post(url, keyword);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}