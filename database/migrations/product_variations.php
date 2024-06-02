use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class AddProductVariations extends Migration
{
    public function up()
    {
        Schema::create('product_variations', function (Blueprint $table) {
            $table->id();
            $table->foreignId('product_id')->constrained()->onDelete('cascade');
            $table->string('name');
            $table->string('description');
            $table->decimal('price', 10, 2);
            $table->integer('stock');
            $table->timestamps();
        });

        Schema::create('product_variation_options', function (Blueprint $table) {
            $table->id();
            $table->foreignId('product_variation_id')->constrained()->onDelete('cascade');
            $table->string('name');
            $table->string('value');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('product_variation_options');
        Schema::dropIfExists('product_variations');
    }
}
