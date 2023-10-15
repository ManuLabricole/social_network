// conversationStore.js
import { defineStore } from 'pinia';
import axios from 'axios';


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
