<template>
	<div class="main-center col-span-3 space-y-4">
		<div class="bg-white border border-gray-200 rounded-lg">
			<div class="flex flex-col flex-grow p-4">
				<MessageReceived />
				<MessageReceived />
				<MessageSent />
				<MessageReceived />
				<!-- 
    FILEPATH: /Users/manulabricole/Documents/Bricolerie/web_dev_tutorials/social_network/frontend/src/components/conversation/Conversation.vue
    This component renders the conversation view and includes the MessageSent component.
-->
				<MessageSent />
			</div>
		</div>

		<div class="bg-white border border-gray-200 rounded-lg">
			<div class="p-4">
				<textarea
					class="p-4 w-full bg-gray-100 rounded-lg resize-none"
					placeholder="What do you want to say?"></textarea>
			</div>

			<div class="p-4 border-t border-gray-100 flex justify-between">
				<a
					href="#"
					class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
					>Post</a
				>
			</div>
		</div>
	</div>
</template>

<!--
FILEPATH: /Users/manulabricole/Documents/Bricolerie/web_dev_tutorials/social_network/frontend/src/components/conversation/Conversation.vue
-->

<script>
	/**
	 * @name ConversationView
	 * @description A component that displays a conversation between two users.
	 * @component
	 *
	 * @example
	 * <ConversationView />
	 */
	import MessageSent from './MessageSent.vue';
	import MessageReceived from './MessageReceived.vue';
	import { useConversationStore } from '@/stores/conversationStore';

	export default {
		name: 'ConversationView',
		components: {
			MessageSent,
			MessageReceived,
		},
		props: {
			activeConversationId: {
				type: [String, Number],
				required: false,
			},
		},
		setup() {
			const conversationStore = useConversationStore();
			return {
				conversation: conversationStore.conversation,
			};
		},
	};
</script>

<style lang="scss" scoped></style>
