use BotMan\BotMan\BotMan;
use BotMan\BotMan\BotManFactory;
use BotMan\BotMan\Drivers\DriverManager;

class ChatbotController extends Controller
{
    public function handleChatbot(Request $request)
    {
        DriverManager::loadDriver('Telegram');

        $botman = BotManFactory::create();

        $botman->hears('Hello', function (BotMan $bot) {
            $bot->reply('Hello! How can I help you?');
        });

        $botman->listen();
    }
}
