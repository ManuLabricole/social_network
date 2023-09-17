<template>
	<div class="main-right col-span-1 space-y-4">
		<PeopleYouMayKnow />
		<Trends />
	</div>
</template>

<script>
	import PeopleYouMayKnow from '../../components/feed/PeopleYouMayKnow.vue';
	import Trends from '../../components/feed/Trends.vue';
	export default {
		setup() {
			return {};
		},
	};
</script>

<style lang="scss" scoped></style>
