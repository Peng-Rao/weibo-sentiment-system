<script setup>
import {ref, onMounted, onUnmounted} from 'vue';

const message = ref('');
const receivedMessage = ref('');
let ws = null

const connectWebSocket = () => {
    ws = new WebSocket('ws://localhost:8000/ws');
    ws.onmessage = (event) => {
        receivedMessage.value = event.data;
    };

    ws.onclose = () => {
        console.log('WebSocket disconnected. Reconnecting...');
        setTimeout(connectWebSocket, 1000);
    };
}

const sendMessage = () => {
    if (message.value.trim()) {
        ws.send(message.value);
        message.value = ''; // Clear input after sending
    }
};

onMounted(() => {
    connectWebSocket();
});
onUnmounted(() => {
  if (ws.value && ws.value.readyState === WebSocket.OPEN) {
    ws.value.close();
    console.log('WebSocket connection closed by component unmount.');
  }
});
</script>

<template>
  <div>
    <input v-model="message" @keyup.enter="sendMessage" placeholder="Type a message">
    <button @click="sendMessage">Send</button>
    <p>Received: {{ receivedMessage }}</p>
  </div>
</template>

<style scoped>

</style>