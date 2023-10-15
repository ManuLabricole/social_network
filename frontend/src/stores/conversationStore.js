// conversationStore.js
import { defineStore } from 'pinia';
import axios from 'axios';


export const useConversationStore = defineStore('conversation', {
    state: () => ({
        userId: null,
        conversations: [],
        selectedConversation: null,
        messages: [],
        isLoading: false,
    }),
    actions: {
        setUserId(userId) {
            this.userId = userId;
            console.log(userId);
        },
        async fetchConversations() {
            this.isLoading = true;
            try {
                const response = await axios.get('/api/v1/users/conversations/me/');
                this.conversations = response.data;
                console.log(response);
            }
            catch (err) {
                console.log(err);
            }
            finally {
                this.isLoading = false;
            }
        },
        async fetchMessages(conversationId) {
            // Fetch messages for a specific conversation
            // this.messages = await apiCallToFetchMessages(conversationId);
        },
        async sendMessage(conversationId, message) {
            // Send a new message
            // await apiCallToSendMessage(conversationId, message);
        },
        selectConversation(conversation) {
            this.selectedConversation = conversation;
        },
    },
});
