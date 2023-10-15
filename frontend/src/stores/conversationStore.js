// conversationStore.js
import { defineStore } from 'pinia';

export const useConversationStore = defineStore('conversation', {
    state: () => ({
        conversations: [],
        selectedConversation: null,
        messages: [],
    }),
    actions: {
        async fetchConversations() {
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
