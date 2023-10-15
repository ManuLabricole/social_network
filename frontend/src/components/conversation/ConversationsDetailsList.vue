<template>
	<div class="main-left col-span-1">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<div
				class="space-y-6"
				v-for="conversation in conversationStore.conversations"
				:key="conversation.id"
				@click="setActiveConversation(conversation.id)">
				<ConversationDetails
					:conversation="conversation"
					:isSelected="
						conversationStore.selectedConversation.id === conversation.id
					"
					:currentUserId="conversationStore.userId" />
			</div>
		</div>
	</div>
</template>

<script>
	import ConversationDetails from './ConversationDetails.vue';
	import { useConversationStore } from '@/stores/conversationStore';

	export default {
		name: 'ConversationDetailsList',
		components: {
			ConversationDetails,
		},
		setup() {
			const conversationStore = useConversationStore();

			const setActiveConversation = (id) => {
				conversationStore.setSelectedConversation(id); // Update the store
			};

			return {
				conversationStore,
				setActiveConversation, // Make the method available to the template
			};
		},
		mounted() {
			this.conversationStore.fetchConversations();
		},
	};
</script>

<style scoped></style>
