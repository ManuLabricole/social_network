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
                this.setSelectedConversation(this.conversations[0].id);
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
        setSelectedConversation(conversationId) {
            const conversation = this.conversations.find(c => c.id === conversationId);
            if (conversation) {
                this.selectedConversation = conversation;
                // Optionally, fetch messages for the selected conversation
                this.fetchMessages(conversationId);
            }
        },
    },
});
