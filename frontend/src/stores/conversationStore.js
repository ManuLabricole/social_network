// conversationStore.js
import { defineStore } from 'pinia';

export const useConversationStore = defineStore('conversation', {
    state: () => ({
        conversations: [],
        selectedConversation: null,
        messages: [],
        isLoading: false,
    }),
    actions: {
        async fetchConversations() {
            this.isLoading = true;
            try {
                const response = await this.$axios.get('/api/v1/conversations/');
                this.conversations = response.data;
            }
            catch (err) {
                console.log(err);
            }
            finally {
                this.isLoading = false;
            }
            // Fetch conversations from API and update state
            // this.conversations = await apiCallToFetchConversations();
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