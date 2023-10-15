<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<ConversationDetailsList
			@active-conversation-changed="setActiveConversation" />
		<Conversation :activeConversationId="activeConversationId" />
	</div>
</template>

<script>
	import ConversationDetailsList from '@/components/conversation/ConversationsDetailsList.vue';
	import Conversation from '@/components/conversation/Conversation.vue';
	import { useConversationStore } from '@/stores/conversationStore';
	import { useUserStore } from '@/stores/user';

	export default {
		name: 'ConversationView',
		components: {
			ConversationDetailsList,
			Conversation,
		},
		setup() {
			const conversationStore = useConversationStore();
			const userStore = useUserStore();
			conversationStore.setUserId(userStore.user.id);
			return {};
		},
		data() {
			return {
				activeConversationId: null,
			};
		},
		methods: {
			setActiveConversation(id) {
				this.activeConversationId = id;
				console.log('active conversation changed', id);
			},
		},
	};
</script>

<style scoped></style>
