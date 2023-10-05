from discord import Embed


class Utils:
    def validate_args(*args, **kwargs) -> bool:
        return all(args) and all(kwargs)

    @staticmethod
    def get_snipe_embed() -> Embed:
        embed = Embed()
        return embed
